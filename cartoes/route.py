from flask import(
    Blueprint, 
    request, 
    flash, 
    redirect, 
    url_for, 
    render_template, 
    jsonify
)
from cartoes.form import CardForm
from cartoes.controller import(
    create_card, 
    list_all_card, 
    list_card_id, 
)


bp = Blueprint('card', __name__)


@bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template("index.html", title="Card")


@bp.route("/card/register", methods=['GET', 'POST'])
def register_card():
    form = CardForm()
    if request.method == "POST":
        if form.validate_on_submit():
            
            create_card(
                number=form.number.data,
                ccv=form.ccv.data,
                situation=form.situation.data
                )

            flash('Card ' + form.number.data + ' has benn created!', 'success')
            return redirect(url_for('card.register_card'))
            
    return render_template('create_card.html', title='Card Create', form=form)


@bp.route("/card/list", methods=['GET', 'POST'])
def list_card():
    cards = list_all_card()
    if not cards:
        flash('There are no records. Register a Group', 'error')
        return redirect(url_for('card.index'))
    return render_template("list_card.html", title='Card List', cards=cards)


@bp.route("/consult", methods=['POST'])
def consult_card():
    _json = request.json
    _id = _json["id"]
    
    card = list_card_id(_id)
    number = card.number
    ccv = card.ccv
    situation = card.situation

    return  jsonify(number=number, ccv=ccv, situation=situation)
    



