from deep_translator import GoogleTranslator

# source="lingua original", traget="lingua alvo"
tradutor = GoogleTranslator(source="en", target="pt")

text = """
A system administrator at Lawrence Berkley National Labs, Clifford Stoll, documented his personal hunt for a hacker (and KGB informant)
"""

tradutor = tradutor.translate(text)

print(tradutor)
