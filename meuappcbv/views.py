import requests
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import ViaCep
from .forms import ViaCepForm


class ViaCepFormView(FormView):
    template_name = "meuappcbv/forms.html"
    form_class = ViaCepForm
    success_url = reverse_lazy("viacep_list")

    def form_valid(self, form):
        cep = form.cleaned_data["cep"].replace("-", "").strip()
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if "erro" not in data:
                cep_obj, created = ViaCep.objects.update_or_create(
                    cep=cep,
                    defaults={
                        "logradouro": data.get("logradouro", ""),
                        "bairro": data.get("bairro", ""),
                        "localidade": data.get("localidade", ""),
                        "uf": data.get("uf", ""),
                    },
                )
                self.object = cep_obj
            else:
                form.add_error("cep", "CEP não encontrado")
                return self.form_invalid(form)
        else:
            form.add_error("cep", "Erro ao consultar o CEP")
            return self.form_invalid(form)

        return super().form_valid(form)
# Create your views here.
