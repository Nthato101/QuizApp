from django.shortcuts import render ,redirect
from .question_set import Question
from .quiz_logic import QuizBrain
from .models import Player
from .forms import Registration_Form, Login_form
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    player_list = Player.objects.filter(has_played=True).order_by('-score')
    if player_list:
        context = {
            'players':player_list
        }
    else:
        context = {
            'message': 'No players yet'
        }
    return render(request,'index_sec.html',context=context)
def quiz_setup():
    question_list =[ 
                            {
                                'question':'David Beckham became president of which newly founded club in 2018?',
                                'opt1':'Bergamo Calcio',
                                'opt2':'Inter Miami',
                                'opt3':'West London Blue',
                                'opt4': 'The Potteries',
                                'answer':'Inter Miami' 
                            },
                            {
                                'question':'Who won the Man of the Match award in the 2014 World Cup final?',
                                'opt1':'Mario Goetze',
                                'opt2':'Sergio Aguero',
                                'opt3':'Lionel Messi',
                                'opt4': 'Bastian Schweinsteiger',
                                'answer':'Lionel Messi'
                            },
                            {
                                'question':'Which footballer holds the record for the highest number of assists in the Premier League?',
                                'opt1':'Cesc Fabregas',
                                'opt2':'Ryan Giggs',
                                'opt3':'Frank Lampard',
                                'opt4': 'Paul Scholes',
                                'answer':'Ryan Giggs' 
                            },
                            {
                                'question':'Jamie Vardy was signed by Leicester from which non-league side?',
                                'opt1':'Ketting Town',
                                'opt2':'Alfreton Town',
                                'opt3':'Grimsby Town',
                                'opt4': 'Fleetwood Town',
                                'answer':'Fleetwood Town'
                            },
                            {
                                'question':' Chelsea beat which team 8-0 to secure the 2009-10 Premier League title on the final day of the season?',
                                'opt1':'Blackburn',
                                'opt2':'Hull',
                                'opt3':'Wigan',
                                'opt4': 'Norwich',
                                'answer':'Wigan' 
                                },
                            {
                                'question':'Manchester United beat which team in the 2017 Europa League final?',
                                'opt1':'Villarreal',
                                'opt2':'Chelsea',
                                'opt3':'Ajax',
                                'opt4': 'Borussia Dortmund',
                                'answer':'Ajax'
                            },
                            {
                                'question':'Which team did Porto beat in the 2004 Champions League final?',
                                'opt1':'Bayern Munich',
                                'opt2':'Deportivo La Coruña',
                                'opt3':'Barcelona',
                                'opt4': 'Monaco',
                                'answer':'Monaco' 
                            },
                            {
                                'question':'What was the score in the Euro 2012 final?',
                                'opt1':'1-0',
                                'opt2':'3-0',
                                'opt3':'5-0',
                                'opt4': '4-0',
                                'answer':'4-0'
                            },]
    question_bank = []
    for item in question_list:
        new_question = Question(item)
        question_bank.append(new_question)
    return question_bank
@login_required
def quiz(request):
    if request.method == 'POST':
            quiz_questions = quiz_setup()
            quiz_run = QuizBrain(request,quiz_questions)
            index = int(request.POST['index']) - 1
            current = int(request.POST['score'])
            quiz_run.question_number = index 
            answer = quiz_questions[index].answer
            user_answer = ''
            if 'exampleRadios' in request.POST:
                user_answer = request.POST['exampleRadios']
            quiz_run.score = current + quiz_run.score_check(user_answer,answer)
            if quiz_run.still_has_question():
                quiz_run.next_question()
                index = quiz_run.question_number
                context = {
                    'question': quiz_questions[index],
                    'question_number':index+1,
                    'total_questions':len(quiz_questions),
                    'score':quiz_run.score
                }

                player = Player.objects.get(user=request.user.id)
                player.score = quiz_run.score
                player.has_played = True
                player.save()
                return render(request,'quiz_sec.html',context=context)
            else:
                player = Player.objects.get(user=request.user.id)
                player.score = quiz_run.score
                player.has_played = True
                player.save()
                context = {'player':player}
                return render(request,'pre_quiz.html',context=context)
    quiz_questions = quiz_setup()
    quiz_run = QuizBrain(request,quiz_questions)
    index = 0
    context = {
        'question': quiz_run.question_list[index],
        'question_number':index + 1,
        'total_questions':len(quiz_questions),
        'score':quiz_run.score
    }
    return render(request,'quiz_sec.html',context=context)
    
@login_required
def pre_quiz(request):
        player = Player.objects.get(user=request.user.id)
 
        context = {
            'player':player
        }
        return render(request,'pre_quiz.html',context=context)

def login_page(request):
    form = Login_form()
    context = {
        'form': form
    }

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request=request,username=email,password=password)
        if user is not None:
            login(request,user)
            player_list = Player.objects.filter(has_played=True).order_by('-score')
            if player_list:
                context = {
                    'players':player_list,
                    'message':'You have logged in successfully'
                }
            else:
                context = {
                    'message': 'No players yet'
                }
            return render(request,'index_sec.html',context=context)
        else:
            return render(request,'login.html',context=context)
            
    return render(request,'login.html',context=context)
    
def logout_user(request):
    logout(request)
    return redirect('homepage')

def register_user(request):
    form = Registration_Form()

    context = {
        "form":form
    }

    if request.method == 'POST':
        form = Registration_Form(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = authenticate(email=email,password=password)
            player = Player(user = user, first_name=first_name,last_name=last_name,password = user.password)
            player.save()
            login(request,user)
            context = {
                'message': 'You have successfully registered'
            }
            return render(request,'pre_quiz.html',context)
        else:
            context = {
                "form":form
                }

            return render(request,'register.html',context)

    return render(request,'register.html',context)