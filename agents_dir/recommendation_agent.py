from openai import OpenAI
client = OpenAI()


def get_recommendation(fraud_result, sla_result, interest_rate_result):
    prompt = f"""
    You are a loan decision assistant. Based on SLA compliance, fraud risk results, and interest rate results, write a concise recommendation on whether to approve or reject the loan application.
    Here is the sla result: {sla_result}
    Here is the fraud result: {fraud_result}
    Here is the interest rate result: {interest_rate_result}

    Return your recommendation.
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        temperature=0.1
    )
    return response.output_text
