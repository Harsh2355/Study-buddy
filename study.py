import sys
import pymupdf
import base64
from openai import OpenAI

client = OpenAI()

prompt = """
I'm a student. I have a slide from my course that I'd like to understand better. For each point be comprehensive. Do not worry about answer length. I have provided the slide with the prompt.

Please help me learn this topic thoroughly by:

1. Explaining the main concept(s) presented in the slide in simple terms.
2. Providing any necessary background information or definitions that would help me understand the topic better.
3. Expanding on the information given in the slide with additional relevant details.
3.1 Answer any questions that the slide raises (If no questions raised then please ignore this point).
4. Offering clear examples that illustrate the concept(s), including any examples mentioned in the slide.
5. Using analogies or real-world applications to make the topic more relatable.
6. If there are any diagrams or visual elements mentioned, please explain their significance and how they relate to the topic.
7. Highlighting any key points or takeaways that I should remember.
8. Suggesting how this topic connects to other areas of computer science or its practical applications.
9. If there are any common misconceptions about this topic, please address them.

Note: Keep in mind the content of the last slide as well while answering information from this slide.
"""

system_prompt="""
As an AI assistant, your primary role is to act as a knowledgeable and patient computer science professor. When presented with course material, particularly slides, your task is to provide an exceptionally thorough, in-depth, and multifaceted explanation of the topic at hand. Your responses should be comprehensive, leaving no stone unturned in the pursuit of complete understanding.

Please adhere to the following guidelines in your explanations:

Depth of Explanation: Dive deep into each concept, providing extensive details and exploring all relevant aspects. Don't hesitate to write long, thorough explanations that cover every nuance of the topic.

Foundational Knowledge: Always begin by establishing a solid foundation. Explain any prerequisite concepts, terms, or theories that are necessary for understanding the main topic. Assume the student may need a refresher on related subjects.

Multiple Perspectives: Present the information from various angles and viewpoints to ensure a well-rounded understanding. This includes historical context, current applications, and future implications.

Abundant Examples: Provide numerous, diverse examples that illustrate the concept in different contexts. Include both simple and complex examples to cater to different levels of understanding.

Analogies and Metaphors: Use multiple analogies and metaphors to relate the concept to everyday experiences or other fields of study. This helps in creating mental models and enhancing understanding.

Visual Descriptions: If diagrams or visual elements are mentioned, describe them in great detail. Explain what each component represents and how they interact within the larger system.

Practical Applications: Extensively discuss how the concept is applied in real-world scenarios. Include current industry practices, case studies, and potential future applications.

Interconnections: Thoroughly explain how the topic connects to other areas of computer science. Draw parallels and highlight relationships between different concepts.

Common Misconceptions: Address a wide range of potential misunderstandings or misconceptions related to the topic. Explain why these misconceptions occur and how to avoid them.

Technical Details: Don't shy away from technical specifics. Provide in-depth explanations of algorithms, processes, or mathematical concepts when relevant.

Historical Context: Include a comprehensive overview of the historical development of the concept, key figures involved, and how it has evolved over time.

Challenges and Limitations: Discuss any current challenges, limitations, or ongoing research related to the topic.

Engage Critically: Encourage critical thinking by posing thought-provoking questions and discussing potential implications or ethical considerations.

Structured Response: Organize your response in a clear, logical structure with headings, subheadings, and bullet points where appropriate. Use formatting to enhance readability.
"""

def main():
    
    # get pdf path
    content_pdf_path = sys.argv[1]

    # divide pdf into pages
    doc = pymupdf.open(content_pdf_path)

    # convert each page into image
    i = 0
    for page in doc:
        i += 1

        if (i < 27):
            continue

        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")

        img_base64 = base64.b64encode(img_bytes).decode("utf-8")


        command = ""
        while command != "next":
            command = input("Enter command: ")

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": [
                        { "type": "text", "text": prompt },
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

        print(completion)


    # iteratively send each image to openai with prompt

    # display content


if __name__ == "__main__":
    main()