from signs import signs
print("Answer the options by\n Pressing 1 for yes and 0 for No")
Questions = ["Do you have a Sharp Headache\n1.Yes\n0.No\n\n",
                 "Do you have a fever\n1.Yes\n0.No\n\n",
                 "Do you have general boby weakness\n1.Yes\n0.No\n\n",
                 "Do you have a high temperature\n1.Yes\n0.No\n\n"
                 ]

Answers = [signs(Questions[0],"1"),
               signs(Questions[1],"1"),
               signs(Questions[2],"1"),
               signs(Questions[3],"1")
               ]
def malaria(Questions):
    score = 0
    for mal in Answers:
        answer = input(mal.prompt)

        if answer == mal.answer:
            score += 1
    print(f'You have {score} signs')
    list=[1,2,3,4]
    if score == list[0]:
        print("Normal")
    elif score == list[1]:
        print("Take a rest")
    elif score == list[2]:
        print("Go to the nearby clinic for further check up")
    elif score == list[3]:
        print("You might be sick,please go to the nearby clinic for malaria check up")
    else:
        print("You are ok")


malaria(Questions)



