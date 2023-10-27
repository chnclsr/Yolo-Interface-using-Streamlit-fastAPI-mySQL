from typing import List

class TableColumnsKeyGenerator:
    def create_params_prompt(self, columns: List):
        prompt = "("
        for column in columns:
            prompt += f"{column}, "
        # remove ', ' from prompt
        prompt = prompt[:-2]
        prompt += ")"
        return prompt