from flask import Flask,jsonify,render_template
from flask_sqlalchemy import SQLAlchemy
import random

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
db = SQLAlchemy()
db.init_app(app)


class Try(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.TEXT,nullable=True)
    platform=db.Column(db.TEXT,nullable=True)
    release_date=db.Column(db.TEXT,nullable=True)
    summary=db.Column(db.TEXT,nullable=True)
    review=db.Column(db.Float,nullable=True)

# with app.app_context():
#     db.create_all()
    
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/game")
def game():
    ranum=random.randint(1,18000)
    game = db.session.execute(db.select(Try).filter_by(id=ranum)).scalar_one()
    user={
        "id":game.id,
        "name":game.name,
        "platform":game.platform,
        "date":game.release_date,
        "summary":game.summary,
        "review":game.review
    }
    return jsonify(user)

@app.route("/games")
def games():
    games = db.session.execute(db.select(Try).order_by(Try.id)).scalars()
    list_c=[]
    # print(type(f"{games}\n\n"))
    for game in games:
        user={
            "id":game.id,
            "name":game.name,
            "platform":game.platform,
            "date":game.release_date,
            "summary":game.summary,
            "review":game.review
        }
        list_c.append(user)
    l=len(list_c)
    matter={"total":l,
            "games":list_c}

    return jsonify(matter)

@app.route("/top")
def top():
    games = db.session.execute(db.select(Try).order_by(Try.review.desc())).scalars()
    list_c=[]

    for game in games:
        if game.review > 9:
            user={
                "id":game.id,
                "name":game.name,
                "platform":game.platform,
                "date":game.release_date,
                "summary":game.summary,
                "review":game.review
            }
            list_c.append(user)

    l=len(list_c)
    matter={"total":l,
            "games":list_c}
    return jsonify(matter)

@app.route("/ps4")
def ps4():
    games = db.session.execute(db.select(Try).order_by(Try.id)).scalars()
    list_c=[]
    for game in games:
        if game.platform=="PlayStation 4":
            user={
                "id":game.id,
                "name":game.name,
                "platform":game.platform,
                "date":game.release_date,
                "summary":game.summary,
                "review":game.review
            }
            list_c.append(user)
    l=len(list_c)
    matter={"total":l,
            "games":list_c}

    return jsonify(matter)

@app.route("/ps2")
def ps2():
    games = db.session.execute(db.select(Try).order_by(Try.id)).scalars()
    list_c=[]
    for game in games:
        if game.platform=="PlayStation 2":
            user={
                "id":game.id,
                "name":game.name,
                "platform":game.platform,
                "date":game.release_date,
                "summary":game.summary,
                "review":game.review
            }
            list_c.append(user)
    l=len(list_c)
    matter={"total":l,
            "games":list_c}

    return jsonify(matter)

@app.route("/pc")
def pc():
    games = db.session.execute(db.select(Try).order_by(Try.id)).scalars()
    list_c=[]
    for game in games:
        if game.platform=="PC":
            user={
                "id":game.id,
                "name":game.name,
                "platform":game.platform,
                "date":game.release_date,
                "summary":game.summary,
                "review":game.review
            }
            list_c.append(user)
    l=len(list_c)
    matter={"total":l,
            "games":list_c}

    return jsonify(matter)
if __name__=="__main__":
    app.run(debug=True)