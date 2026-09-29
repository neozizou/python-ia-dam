# Lista de comprobación antes de desplegar

## Repositorio
- [ ] `requirements.txt` con versiones fijadas (`pandas==3.0.2`, no `pandas`)
- [ ] La misma versión de scikit-learn con la que entrenaste el modelo
- [ ] `.gitignore` con `.venv/`, `__pycache__/` y los ficheros de datos pesados
- [ ] Ninguna contraseña, clave de API ni URL con credenciales en el código
- [ ] `README.md` con puesta en marcha, hallazgos y ficha del modelo

## Datos y modelo
- [ ] Los datos publicados son públicos y no contienen datos personales
- [ ] El modelo entrenado está accesible para la aplicación (en el repositorio si es pequeño)
- [ ] Las rutas se construyen con `Path(__file__)`, no con rutas absolutas de tu equipo

## Aplicación
- [ ] `@st.cache_data` para los datos y `@st.cache_resource` para el modelo
- [ ] Mensaje claro si falta el modelo o el fichero de datos
- [ ] Aviso cuando la entrada del usuario queda fuera del rango de entrenamiento
- [ ] Cada predicción se muestra con su margen de error
- [ ] Probada en local con `streamlit run` antes de publicar

## Publicación
- [ ] Desplegada en share.streamlit.io y abierta desde otro dispositivo
- [ ] El enlace está en el `README.md` del repositorio
