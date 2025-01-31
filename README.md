# Install:
```commandline
pip install trengine
```

# About this project:
- TREngine is python library based on 4 translators engines:
- Ajax ( [translate.com](https://www.translate.com/translator) )
- Google ( [translate.google.com](https://translate.google.com/) )
- Hozory ( [hozory.com](https://hozory.com/FA) )
- Translatedict ( [translatedict.com](https://www.translatedict.com/) )

- Supporting Sync & Async.

# How to use?
- Here an example to use it:
```python
from trengine import Engine

eng = Engine()
text = "Hola, mi amor"

print(
    eng.google.translate(text, "en"), "\n",
    eng.ajax.translate(text, "en"), "\n",
    eng.hozory.translate(text, "en"), "\n",
    eng.tdict.translate(text, "en"), "\n",
)
```
- Here an async example:
```python
import asyncio
from trengine import AsyncEngine

eng = AsyncEngine()
text = "Hola, mi amor"

async def main():
    print(
        await eng.google.translate(text, "en"), "\n",
        await eng.ajax.translate(text, "en"), "\n",
        await eng.hozory.translate(text, "en"), "\n",
        await eng.tdict.translate(text, "en"), "\n",
    )

asyncio.run(main())
```