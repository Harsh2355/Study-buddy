import sys
import pymupdf
import base64
from enum import Enum
from static_prompts import SYSTEM_PROMPT, USER_PROMPT, USER_INPUT_REQUEST
from openai import OpenAI

client = OpenAI()

class UserInputType(Enum):
    NEXT_SLIDE = "n"
    SKIP_SLIDE = "s"
    QUIT = "q"

def main():
    
    # get pdf path
    content_pdf_path = sys.argv[1]

    # divide pdf into pages
    doc = pymupdf.open(content_pdf_path)

    # convert each page into image
    page_no = 1
    for page in doc:

        print(f"Page {page_no}")
        page_no += 1
        command = input(USER_INPUT_REQUEST).strip().lower()
        while command not in {item.value for item in UserInputType}:
            command = input(USER_INPUT_REQUEST).strip().lower()

        if command == UserInputType.SKIP_SLIDE.value:
            continue
        elif command == UserInputType.QUIT.value:
            print("Quitting...")
            break

        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")

        img_base64 = base64.b64encode(img_bytes).decode("utf-8")

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": [
                        { "type": "text", "text": USER_PROMPT },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{img_base64}",
                            },
                        },
                    ],
                }
            ],
        )
        print(completion.choices[0].message.content + "\n\n\n")


    # iteratively send each image to openai with prompt

    # display content


if __name__ == "__main__":
    main()