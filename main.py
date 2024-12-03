from colorthief import ColorThief
import os
import replicate

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def extract_skin_tone(image_path):
    ct = ColorThief(image_path) #colorthief_object
    return(ct.get_color(quality=1))

os.environ["REPLICATE_API_TOKEN"] = "your-api-token" 

def extract_optimum_colors(image_path):
    skin_tone = extract_skin_tone(image_path)
    prompt = f"""
                Analyze the skin tone represented by the rgb color `{skin_tone}`. 
                Provide a comprehensive color analysis, including:
                Complementary colors: Colors that contrast beautifully with the skin tone.
                Harmonious colors: Colors that blend well with the skin tone.
                Accent colors: Bold colors that can be used to add a pop of color.
                For each color category, give top 5 colour rgb values and provide a brief explanation.
                """
    output = replicate.run(
    "meta/llama-2-70b-chat",
    input={"prompt": prompt,
         "system_prompt": "You are a people's colour analyst. Your aim is to enhance style and provide colours that look good on a person based on his/her skin tone, extracted from a picture they uploaded. Focus on colour theory",
         "max_tokens":1200})
    return output