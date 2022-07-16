from flask import Flask

# Importing a blueprints
from app.main.views import main_blueprint
from app.candidates.views import candidates_blueprint
from app.vacancies.views import vacancies_blueprint

# Create a flask instance
app = Flask(__name__)

# Registering a blueprints
app.register_blueprint(main_blueprint)
app.register_blueprint(candidates_blueprint)
app.register_blueprint(vacancies_blueprint)

# Starting the server only if the file is running and not imported
if __name__ == "__main__":
    app.run()
