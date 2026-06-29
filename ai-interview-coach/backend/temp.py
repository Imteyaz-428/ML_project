from services.providers.deepseek_provider import DeepSeekProvider

provider = DeepSeekProvider()

response = provider.generate("""
Return ONLY JSON

{
    "name":"DeepSeek",
    "status":"working"
}
""")

print(response)