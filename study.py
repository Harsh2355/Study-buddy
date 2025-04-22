import sys
import pymupdf
import base64
from enum import Enum
from static_prompts import SYSTEM_PROMPT, USER_PROMPT, USER_INPUT_REQUEST
from openai import OpenAI

client = OpenAI()

class UserInputType(Enum):
    NEXT_SLIDE = "n"
    BATCH_SLIDE = "b"
    PREVIOUS_SLIDE = "p"
    SKIP_SLIDE = "s"
    ASK_QUESTION = "a"
    GO_TO_PAGE = "g"
    QUIT = "q"

def ask_question(question):
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
                        { "type": "text", "text": question },
                    ]
                }
            ]
    )
    return completion.choices[0].message.content

def main():
    
    # get pdf path
    content_pdf_path = sys.argv[1]

    # divide pdf into pages
    doc = pymupdf.open(content_pdf_path)

    # convert each page into image
    page_no = 0
    while page_no < len(doc):

        print(f"Page {page_no + 1}")
        command = input(USER_INPUT_REQUEST).strip().lower()
        while command not in {item.value for item in UserInputType}:
            command = input(USER_INPUT_REQUEST).strip().lower()

        if command == UserInputType.SKIP_SLIDE.value:
            page_no += 1
            print("\n")
            continue
        elif command == UserInputType.GO_TO_PAGE.value:
            cur_num = page_no
            page_no = int(input("Enter page number: ")) - 1
            if page_no < 0 or page_no >= len(doc):
                print("Invalid page number. Please try again.")
                page_no = cur_num
            print("\n")
            continue
        elif command == UserInputType.BATCH_SLIDE.value:
            num_batch_pages = int(input("Enter the number of pages to batch: "))
            page = doc[page_no : page_no + num_batch_pages]
            page_no += num_batch_pages
        elif command == UserInputType.NEXT_SLIDE.value:
            page = [doc[page_no]]
            page_no += 1
        elif command == UserInputType.ASK_QUESTION.value:
            question = input("Enter your question: ")
            print(ask_question(question))
            print("\n")
            continue
        elif command == UserInputType.PREVIOUS_SLIDE.value:
            page_no -= 1
            print("\n")
            continue
        elif command == UserInputType.QUIT.value:
            print("Quitting...\n")
            break

        user_content = {
            "role": "user",
            "content": [
                { "type": "text", "text": USER_PROMPT },
            ]
        }

        for p in page:
            pix = p.get_pixmap()
            img_bytes = pix.tobytes("png")
            img_base64 = base64.b64encode(img_bytes).decode("utf-8")
            user_content["content"].append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{img_base64}",
                },
            })

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT,
                },
                user_content
            ],
        )
        
        print(completion.choices[0].message.content + "\n\n\n")

if __name__ == "__main__":
    main()