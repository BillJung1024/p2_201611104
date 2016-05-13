import turtle
wn=turtle.Screen()

def school():
    School=list()
    School=[
    ["구분","매우 만족","약간 만족","보통","약간 불만족","매우 불만족","평균(점)"],
    ["교육내용", 13.1, 34.6, 39.5, 13.4, 1.9, 3.39],
    ["교우관계",27.1,40.0,28.5,2.9,1.5,3.88],
    ["교사(교수)와의 관계",16.2,37.8,38.4,6.8,0.8,3.62],
    ["학교시설 및 설비",11.4,29.8,39.0,14.8,4.9,3.28],
    ["주변 환경",12.2,26.5,42.0,14.9,4.4,3.27],
    ["전공",13.5,29.7,43.4,11.1,2.4,3.41],
    ["전반적인 학교생활",13.7,37.6,43.4,4.1,1.2,3.59],
    ]
    data=list()
    data=School[1:]
    satisfaction=0
    dissatisfaction=0
    for i in data:
        if i in School:
            satisfaction+=i[1]
            satisfaction+=i[2]
    print satisfaction 
    satisfactionaverage=satisfaction/7
    print "satisfaction average: ",satisfactionaverage

    for i in data:
        if i in School:
            dissatisfaction+=i[4]
            dissatisfaction+=i[5]
    print dissatisfaction
    dissatisfactionaverage=dissatisfaction/7
    print "dissatisfaction average: ",dissatisfactionaverage
def speech():
    Franklin=list()
    Franklin=[
      "MR.Chief Justice, Mr. Vice President, my friends, you will understand and, I believe, agree with my wish that the form of this inauguration be simple and its words brief.",

      "We Americans of today, together with our allies, are passing through a period of supreme test. It is a test of our courage - of our resolve - of our wisdom - our essential democracy.",

      "If we meet that test - successfully and honorably - we shall perform a service of historic importance which men and women and children will honor throughout all time.",

    "As I stand here today, having taken the solemn oath of office in the presence of my fellow countrymen - in the presence of our God - I know that it is America's purpose that we shall not fail.",

    "In the days and in the years that are to come we shall work for a just and honorable peace, a durable peace, as today we work and fight for total victory in war.",

    "We can and we will achieve such a peace.",

    "We shall strive for perfection. We shall not achieve it immediately - but we still shall strive.",

    "We may make mistakes - but they must never be mistakes which result from faintness of heart or abandonment of moral principle.",

    "I remember that my old schoolmaster, Dr. Peabody, said, in days that seemed to us then to be secure and untroubled: Things in life  will not always run smoothly. Sometimes we will be rising toward the heights - then all will seem to reverse itself and start downward. The great fact to remember is that the trend of civilization itself is forever upward; that a line drawn through the middle of the peaks and the valleys of the centuries always has an upward trend.",

    "Our Constitution of 1787 was not a perfect instrument; it is not perfect yet.But it provided a firm base upon which all manner of men, of all races and colors and creeds, could build our solid structure of democracy.",

    "And so today, in this year of war, 1945, we have learned lessons - at a fearful cost - and we shall profit by them.",

    "We have learned that we cannot live alone, at peace; that our own well-being is dependent on the well-being of other nations far away. We have learned that we must live as men, not as ostriches, nor as dogs in the manger.",

    "We have learned to be citizens of the world, members of the human community.",

    "We have learned the simple truth, as Emerson said, that The only way to have a friend is to be one.",

    "We can gain no lasting peace if we approach it with suspicion and mistrust or with fear. We can gain it only if we proceed with the understanding, the confidence, and the courage which flow from conviction.",

    "The Almighty God has blessed our land in many ways. He has given our people stout hearts and strong arms with which to strikemighty blows for freedom and truth. He has given to our country a faith which has become the hope of all peoples in an anguished world.",

    "So we pray to Him now for the vision to see our way clearly - to see the way that leads to a better life for ourselves and for all our fellow men - to the achievement of His will to peace on earth."

    ]
    d = dict()
    for sentence in Franklin:
        words=sentence.split()
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
        c=10
    for k in d:
        if d[k]>c:
            print "Franklin : ",k
    Obama=list()
    Obama=[
    "Hello, this is Senator Barack Obama and today is Thursday, June 8th, 2006.",

    "The topic today is net neutrality. ",
    "The internet today is an open platform where the demand for websites and services dictates success.",
    "You've got barriers to entry that are low and equal for all comers. ",
    "And it's because the internet is a neutral platform that I can put on this podcast and transmit it over the internet without having to go through some corporate media middleman.", 

    "I can say what I want without censorship. ",
    "I don't have to pay a special charge. But the big telephone and cable companies want to change the internet as we know it.",
    "They say they want to create high-speed lanes on the internet and strike exclusive contractual arrangements with internet content-providers for access to those high-speed lanes.",
    "Those of us who can't pony up the cash for these high-speed connections will be relegated to the slow lanes.",

    "Allowing the Bells and cable companies to act as gatekeepers with control over internet access would make the internet like cable.",
    "A producer-driven market with barriers to entry for website creators and preferential treatment for specific sites based not on merit, the number of hits, but on relationships with the corporate gatekeeper.",
    "If there were four or more competitive providers of broadband service to every home, then cable and telephone companies would not be able to create a bidding war for access to the high-speed lanes.", 
    "But here's the problem. More than 99 percent of households get their broadband services from either cable or a telephone company.",

    "So here's my view. We can't have a situation in which the corporate duopoly dictates the future of the internet and that's why I'm supporting what is called net neutrality.",
    "In the House, the Energy and Commerce Committee and the Judiciary Committee reached different conclusions on network neutrality. ",
    "Judiciary Committee members voted to protect net neutrality and commerce voted with the Bells and cable. ",
    "That debate is going to hit the House floor this Friday.",
    "In the Senate, Senators Snowe and Dorgan are leading the fight for net neutrality and I've joined in that effort. ",
    "Senator Inouye, the ranking Democrat of the Commerce Committee, has joined us in this effort as well and he's working with Senator Stevens to put strong network neutrality into any Senate bill that comes before us.",
    "There is widespread support among consumer groups, leading academics and the most innovative internet companies, including Google and Yahoo, in favor of net neutrality.",
    "And part of the reason for that is companies like Google and Yahoo might never have gotten started had they not been in a position to easily access the internet and do so on the same terms as the big corporate companies that were interested in making money on the internet.",

    "I know if you are listening to this podcast that you are going to take an intense interest in this issue as well. ",
    "Congress is going to need to hear your voice because the Bell and cable companies are going to be dedicating millions of dollars to defeating network neutrality.", 
    "So I'll keep you updated on this important issue and I look forward to talking to you guys again next week. Bye-bye."
    ]
    l = dict()
    for sentence in Obama:
        words=sentence.split()
        for word in words:
            if word in l:
                l[word]+=1
            else:
                l[word]=1
    c=6
    for k in l:
        if l[k]>c:
            print "Obama : ", k
def lab10():
    school()
    speech()
def main():
    lab10()

main()
wn.exitonclick()
