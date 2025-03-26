from comunidadeimpressionadora import app

# Para a construção de qualquer formulário é preciso:
# - Criar Formulário - mexer no forms.py e criar uma nova classe
# - Colocar formulario dentro do routes
# - Criar um html para ele se for uma página específica
# - Fazer interação com o BD se for um formulário que precise
#   interagir com o BD

if __name__ == "__main__":
    app.run(debug=True)