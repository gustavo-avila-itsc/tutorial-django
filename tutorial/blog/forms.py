from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Tu nombre")
    texto = forms.CharField(widget=forms.Textarea)
    edad = forms.IntegerField()
    def clean_texto(self):
        texto = self.cleaned_data(["texto"])
        for palabra in ["puto","damian","gustavo","abel"]:
            texto = texto.replace(palabra,"***")
        return texto

    def clean_edad (self):
        edad = self.cleaned_data(["edad"])
        if edad > 18:
            raise forms.ValidationError("Debes ser mayor de edad.")
        return edad
