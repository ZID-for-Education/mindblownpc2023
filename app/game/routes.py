from app.game import bp

from flask import render_template

@bp.route('/')
def index():    
    return render_template('game/index.html')

@bp.route('/ASD')
def ASD():
    return render_template('game/ASD.html')

@bp.route('/ADHD')
def ADHD():
    return render_template('game/ADHD.html')

@bp.route('/game-over')
def gameOver():
    return render_template('game/game-over.html')