class AnonymousSurvey:
    """Collect anonymous answers to a survey question"""
    def __init__(self, question):
        """Store a question, and prepare to store respones"""
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_responses(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        print(self.question)
        for response in self.responses:
            print(f"- {response}")


