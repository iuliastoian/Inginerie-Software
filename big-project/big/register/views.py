from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from accounts.models import Doctor, Nurse

# pentru actiunea de inregistrare utilizator nou
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST) # se instantiaza formularul
        if form.is_valid():                # daca formularul este valid, atunci
            #form.save()

            username_input = response.POST.get('username')  # se extrage username-ul
            password_input = response.POST.get('password1') # se extrage parola
            user = User.objects.create_user(username=username_input, password=password_input) # se creeaza un nou user folosind aceste valori

            if (response.POST['regSelect'] == "Doctor"):    # daca s-a ales inregistrarea ca doctor
                print("User is a doctor.\n")
                # se inregistreaza un nou doctor in baza de date, cu relatie unu-la-unu fata de user-ul creat anterior
                new_doctor = Doctor(full_name=response.POST['full_name'], username=user, email=response.POST.get('email'), is_doctor=True, is_nurse=False)
                new_doctor.save()

            elif (response.POST['regSelect'] == "Nurse"):    # daca s-a ales inregistrarea ca doctor
                print("User is a nurse.\n")
                # se inregistreaza o noua asistenta in baza de date, cu relatie unu-la-unu fata de user-ul creat anterior
                new_nurse = Nurse(full_name=response.POST['full_name'], username=user, email=response.POST.get('email'), is_doctor=False, is_nurse=True)
                new_nurse.save()

        return redirect("/") # redirectionare catre pagina principala home
    else:
        form = RegisterForm() # daca formularul nu este valid, se reincarca formularul
    
    return render(response, "register/register.html", {"form":form}) # se randeaza pagina web dupa template-ul descris

def login_view(response):
    if response.method == "POST":
        form = LoginForm(response.POST) # se instantiaza formularul

        username_input = response.POST.get('username')  # se extrage username-ul
        password_input = response.POST.get('password')  # se extrage parola
        user = authenticate(response, username=username_input, password=password_input) # se incearca autentificarea utilizatorului cu datele introduse

        if user is not None:         # daca exista utilizatorul
            login(response, user)    # se face autentificarea in cont
            find_user = User.objects.get(username=username_input)  # se cauta utilizatorul in lista tuturor de tip User

            # cautam in lista de doctori
            try:
                user_type = Doctor.objects.get(username=find_user)
                print("Logged user is a doctor.")  # daca utilizatorul se gaseste, atunci
                return redirect("/doctor_menu")    # redirectioneaza catre meniul pentru doctori
            except:
                # cautam in lista de asistenti
                try:
                    user_type = Nurse.objects.get(username=find_user)
                    print("Logged user is a nurse.")  # daca utilizatorul se gaseste, atunci
                    return redirect("/nurse_menu")    # redirectioneaza catre meniul pentru asistenti
                except:
                    return redirect("/") # pagina de redirectionare dupa login, si anume pagina principala home
    else:
        form = LoginForm() # daca nu exista utilizatorul, atunci formularul se reincarca
        print("Could not log in.")

    return render(response, "registration/login.html", {"form":form}) # se randeaza pagina web dupa template-ul descris