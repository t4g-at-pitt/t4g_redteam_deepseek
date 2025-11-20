from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from openai import OpenAI
import os
class Model:
    """_summary_
    """
    def __deepseek_init__(self, model_name, device):
        self.deepseek_model_name = model_name
        self.ds_model, self.ds_tokenizer = self.create_deepseek_model(device)
        self.ds_model, self.ds_tokenizer, self.ds_token_ids = self.initialize_token_ids()

        return self.ds_model, self.ds_tokenizer, self.ds_token_ids
    
    def query_mistral(self, prompt):

            completion = self.client.chat.completions.create(
              extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
              },
              max_tokens=1000,
              model="mistralai/mistral-7b-instruct:free",
              messages=[
                {
                  "role": "user",
                  "content": prompt
                }
              ]
            )
            return (completion.choices[0].message.content)
    
    def query_chat(self, prompt):
        completion = self.client.chat.completions.create(
              extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
              },
              max_tokens=1000,
              model="openai/o1-mini",
              messages=[
                {
                  "role": "user",
                  "content": prompt
                }
              ]
            )
        try: 
            return (completion.choices[0].message.content)
        except:
            return "Chat GPT did not accept prompt!"


    def __init__(self, model: str):
        # Prefer DEEPSEEK_API_KEY (used with OpenRouter), else use OPENAI_API_KEY (official OpenAI)
        ds_key = os.getenv("DEEPSEEK_API_KEY")
        oa_key = os.getenv("OPENAI_API_KEY")
        api_key = ds_key or oa_key
        if not api_key:
            raise RuntimeError(
                "No API key found. Set DEEPSEEK_API_KEY (preferred for OpenRouter) or OPENAI_API_KEY in your environment or .env"
            )

        # If we have a DEEPSEEK / OpenRouter key, point the client at openrouter.ai
        # Otherwise, if user provided an OpenAI key, let the client use the default OpenAI endpoint.
        if ds_key:
            self.client = OpenAI(
                base_url="https://openrouter.ai/api/v1",
                api_key=api_key,
            )
        else:
            # don't pass base_url when using real OpenAI API key
            self.client = OpenAI(
                api_key=api_key,
            )

        self.model = model
    
    def query(self, prompt: str) -> str:
        print("querying")
        """Queries model with a prompt

        Args:
            prompt (str): Text prompt to provide model

        Returns:
            str: Model output
        """
        completion = self.client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
                "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
            },
            max_tokens=3000,
            model= self.model,
            messages=[
                {
                "role": "user",
                "content": prompt,\
                }
            ]
        )
        try:
            print("complete")
            return completion.choices[0].message.content
        except:
            print(f"Error generating output: {completion.error['metadata']['raw']}")
            return None
    
    def create_deepseek_model(self, device: str = "auto") -> tuple:
        cached_dir = None
        dtype = torch.bfloat16
        tokenizer = AutoTokenizer.from_pretrained(self.deepseek_model_name, cached_dir=cached_dir)
        model = AutoModelForCausalLM.from_pretrained(
            self.deepseek_model_name,
            torch_dtype=dtype,
            device_map=device,
            cache_dir=cached_dir
        )
        return model, tokenizer
    
    def initialize_token_ids(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model, tokenizer = self.create_deepseek_model(device=device)
        if "Qwen" in self.deepseek_model_name:
            token_ids = {
                "BOS" : 151646,
                "USER" : 151644,
                "ASSISTANT" : 151645,
                "NEWLINE" : 198,
                "THINK_START" : 151648,
                "THINK_END" : 151649,
                "EOS" : 151643
            }
        else:
            raise ValueError(f"Uknown tokens for model {self.deepseek_model_name}")
        return model,tokenizer, token_ids

    def encode_message(self, tokenizer, token_ids, user_message: str, thinking_message: str = " "):
        user_tokens = tokenizer.encode(user_message, add_special_tokens=False)
        thinking_tokens = tokenizer.encode(thinking_message, add_special_tokens=False)
        return[[token_ids['BOS']] + user_tokens + [token_ids['NEWLINE']] + [token_ids["THINK_START"]] + thinking_tokens]

    def get_result(self, encoded_message, model, tokenizer):
        input_ids = torch.tensor(encoded_message).to(model.device)
        attention_mask = torch.ones_like(input_ids).to(model.device)
        with torch.no_grad():
            outputs = model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_length=1500,
                do_sample=False,
                temperature=None,
                top_p=None,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id
            )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return generated_text
    

        
