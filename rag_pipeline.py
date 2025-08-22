import textwrap
from yaspin import yaspin
from retrieval_utils import retrieve
from ollama_utils import ollama_stream


def answer(query: str, encoder, index, chunks):
    retrieved = retrieve(query, encoder, index, chunks)
    context = "\n\n".join(
        f"[Trecho {i+1}]\n{textwrap.shorten(t, 400)}" for i, t in enumerate(retrieved)
    )
    prompt = f"""Use o contexto abaixo para responder a pergunta com base nas informações do PDF.\n\nContexto:\n{context}\n\nPergunta: {query}\nResposta:"""

    print("\n🔹 Pensando...")

    with yaspin(text="Gerando resposta com Ollama...", color="cyan") as spinner:
        response_started = False
        for chunk in ollama_stream(prompt):
            if not response_started:
                spinner.ok("✅")
                print("\n🔹 Resposta:")
                response_started = True
            print(chunk, end="", flush=True)
        if not response_started:
            spinner.fail("💥")
            print("\nErro: não houve resposta do modelo.")
