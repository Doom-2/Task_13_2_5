from flask import Blueprint, render_template
from .dao.candidates_dao import CandidateDAO

# Creating a blueprint
candidates_blueprint = Blueprint('candidates_blueprint', __name__, template_folder="templates")

# Creating a DAO instance
candidates_dao = CandidateDAO("./data/candidates.json")


# Creating a view for all candidates
@candidates_blueprint.get('/candidates')
def page_candidates_all():
    candidates = candidates_dao.get_all()
    return render_template('candidates_index.html', candidates=candidates)


# Creating a view for one candidate
@candidates_blueprint.get('/candidates/<int:pk>')
def page_candidate(pk):
    candidate = candidates_dao.get_by_pk(pk)
    return render_template('candidate_single.html', candidate=candidate)
