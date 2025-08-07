import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatbotAPIView(APIView):
    def post(self, request):
        user_input = request.data.get("question")

        if not user_input:
            return Response({"error": "Aucune question reçue."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Tu es un assistant pour une app éducative agricole."},
                    {"role": "user", "content": user_input}
                ]
            )

            reply = response.choices[0].message.content
            return Response({"reply": reply})

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
