# c:\Users\Chifor\FamilyTreeProject\rxconfig.py
import reflex as rx

config = rx.Config(
    app_name="FamilyTreeProject",
    # --- Añade o modifica esta línea ---
    db_url="mysql+pymysql://root:admin@localhost:3306/familytree"
    # ------------------------------------
    # Otras configuraciones que puedas tener...
)
