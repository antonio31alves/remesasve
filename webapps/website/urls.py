
from django.urls import path
from .views import inicio, quienes_somos, preguntas_frecuentes, tipo_cambio, contactenos
from .views import login, signup


urlpatterns = [
	path('', inicio.as_view(), name="inicio"),
	path('quienes-somos', quienes_somos, name="quienes-somos"),
	path('preguntas-frecuentes', preguntas_frecuentes, name="preguntas-frecuentes"),
	path('tipo-cambio', tipo_cambio, name="tipo-cambio"),
	path('contactenos', contactenos, name="contactenos"),
	path('log-in', login, name="log-in"),
	path('sign-up', signup, name="sign-up"),
]