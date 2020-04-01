from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
from rasa.nlu.constants import ENTITIES
from typing import Any, Optional, Text, Dict, List
import typing
import requests
import json
from myComponents.configs import BERT_NER_URL


class ApiBertNer(Component):
    """
      Get entitys by calling service which provides NER recognition.
    """
    name = "bert_ner"
    provides = ["entities"]
    defaults = {}
    language_list = ["zh"]

    def __init__(self, component_config) -> None:
        super().__init__(component_config)
        self.url = BERT_NER_URL

    def train(self, training_data, cfg, **kwargs):
        pass

    def convert_to_rasa(self, value, confidence):
        entity = {"value": value,
                  "confidence": confidence,
                  "entity": "location",
                  "extractor": "sentiment_extractor"}  # 这里的entity应该根据我门的ner结果进行判断， 这里只做简单的演示

        return entity

    def process(self, message, **kwargs):
        #breakpoint()
        text = message.get("text")
        if text:
            resp = requests.post(self.url, data=json.dumps({"inputs": text})) 
            if resp.status_code == 200:
                # 获取entity
                entities, scores = self.get_entity(resp.json())
                if entities:
                    entities = self.convert_to_rasa(entities, scores)
                    message.set(ENTITIES, message.get(ENTITIES, []) + [entities], add_to_output=True)
    
    def get_entity(self, json_result: Dict) -> List[Text]:
        if not json_result.get("output"):
            # 如果没有结果
            return None, None
        outputs = json_result.get("output")
        entities = []  # [["",""], ["", ""]]
        scores = []
        same_entity_words = []
        same_entity_score = []
        old_entity_class = outputs[0].get("entity").split("-")[-1]
        for output in outputs:  # 在多个entity的情况下这里可能有问题
            new_entity_class = output.get("entity").split("-")[-1]
            if new_entity_class == old_entity_class:
                same_entity_words.append(output.get("word"))
                same_entity_score.append(output.get("score"))
            else:
                entities.append(same_entity_words)
                scores.append(same_entity_score)
                same_entity_words = []
                same_entity_words.append(new_entity_class)
                same_entity_score.append(output.get("score"))
                old_entity_class = new_entity_class
        entities.append(same_entity_words)
        scores.append(same_entity_score)
        # merge tokens to one token
        res_entity = ["".join(same_entity_words) for same_entity_words in entities]
        # average score for each entity
        res_score = [sum(same_entity_score)/len(same_entity_score) for same_entity_score in scores]
        return res_entity, res_score

