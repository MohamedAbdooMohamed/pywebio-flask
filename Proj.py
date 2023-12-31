from functools import *
from pywebio.output import *
from pywebio import start_server
from pywebio import session
from pywebio import pin
from pywebio.input import *
##varia.
meaning = " ان الذكاء الاصطناعي مصطلح شامل للتطبيقات التي تؤدي مهاما معقده كانت تتطلب في الماضي ادخالات بشرية مثل التواصل مع العملاء عبر الانترنت او ممارسة لعبة الشطرنج يستخدم هذا المصطلح غالبا بالتبادل مع مجالاتة الفرعية والتي تشمل التعلم الالي والتعلم العميق و "
important = "من الفوائد الكبيرة للذكاء الاصطناعي أنه يستطيع معالجة كميات هائلة من البيانات دون أي عناء بسرعة وفعالية أكبر بكثير من أي إنسان و يمكن لبرمجيات الذكاء الاصطناعي أيضًا اتخاذ قرارات بدائية بناء على تلك البيانات، ويمكن أن يعلم نفسه استخلاص استنتاجات جديدة منها من خلال العملية التي نسميه التعلم الآلي"
pl = "مجموعة من الأوامر، تكتب وفق قواعد معينة ، ومن ثُمَّ تمر هذه الأوامر بعدة مراحل إلى أن تنفذ على جهاز الحاسوب مثل : "
database = " مجموعة من عناصرِ البيانات المنطقية المرتبطة مع بعضها البعض بعلاقة رياضية، وتتكون قاعدة البيانات من جدول واحد أو أكثر."
c = "سي++ (تنطق: سي بلس بلس)  هي لغة برمجة كائنية، متعددة أنماط البرمجة، مصرفة، سكونية الأنماط. وتضم العديد من ميزات لغات البرمجة عالية المستوى ومنخفضة المستوى. بدأ تطوير هذه اللغة امتدادًا للغة سي تحت اسم (سي مع الأصناف) من قبل بيارن ستروستروب في مختبرات بل عام 1979 وأضيفت العديد من الميزات الأخرى لاحقاً وتغير الاسم عام 1983 ليصبح سي++  من باب الدعابة عبر استخدام معامل الزيادة لجانب اسم لغة سي تأكيداً على أنها لغة سي القادمة ."
logic = False
def app():



    popup( "ما هو الذكاء الاصطناعي ؟ ",[
        put_html("<h4> صنع بواسطة عضو المكتب التنفيذي محمد عبد الخالق  </h4>")

            ])

    put_text( "                                                               بسم الله الرحمن الرحيم              ").style( "font-size:20px")
    put_html(" <marquee> بسم الله الرحمن الرحيم  </marquee>")

    put_text("\n")
    put_image(open('C:\\pic.png','rb').read())





    put_text("\n")
    put_text("                              التعريف ").style("font-size:40px ;color:black")
    put_html('<marquee>التعريف </marquee>')

    put_text("\n")
    #put_text(meaning).style('font-size:23px ;color:blue')
    #put_text("\n")
    put_text(  meaning + important + " ولكنة يفقد العامل الابداعي لدى الاشخاص ويجعل منتجات الشركات متشابهة وايضا قلة فرصة العمل وزياده معدل البطالة ").style("font-size:23px ; color:blue")
    put_text("\n")

    #put_text(" : مميزات وعيوب الذكاء الاصطناعي       ").style("font-size:50px ;color:black")
    put_html('<marquee>مميزات وعيوب الذكاء الاصطناعي  </marquee>').style('font-size:40px')

    put_text("\n")
    put_table([
        [' الشي ','العيب '],
        ['زياده معدل البطالة ','عيب'],
        ['ضعف العنصر الابداعي البشري','عيب'],
        ['قلة الابداع بين الشركات','عيب'],




    ]).style("color:red ; font-size:28px ")

    put_table([
        ['الشي ','الميزه'],
        ['زياده الدقة في جميع المجالات', 'ميزه'],
        ['زياده سهولة القيام بالبحوثات', 'ميزه'],
        ['زيادة دقة تشخصيات الامراض ', 'ميزه']

    ]).style("color:green ; font-size:28px ")
    put_text("\n")
    put_text("\n")
    put_text("\n")

    put_text("                                                 لغات البرمجة                            "           ).style("font-size:30px;color:blue")
    put_text(" ان الذكاء الاصطناعي يتم تصنيعة بواسطة لغات برمجة وهي " +  pl).style("font-size:28px")


    #python
    def python():
        put_text("                                       بايثون                                                                   ").style("font-size:50px")
        put_text("بايثون  هي لغة برمجة، عالية المستوى سهلة التعلم مفتوحة المصدر قابلة للتوسيع، تعتمد أسلوب البرمجة الكائنية  لغة بايثون هي لغة مُفسَّرة، ومُتعدِدة الاستخدامات، وتستخدم بشكل واسع في العديد من المجالات، كبناء البرامج المستقلة باستخدام الواجهات الرسومية وفي تطبيقات الويب، ويمكن استخدامها كلغة برمجة نصية للتحكم في أداء العديد من البرمجيات مثل بلندر. بشكل عام، يمكن استخدام بايثون لعمل البرامج البسيطة للمبتدئين، ولإنجاز المشاريع الضخمة في الوقت نفسه. غالباً ما يُنصح المبتدؤون في ميدان البرمجة بتعلم هذه اللغة لأنها من بين أسرع اللغات البرمجية تعلماً.").style('font-size:24px')
    put_text("1 : Python ").style("font-size:24px")
    put_image(open('C:\\python.png','rb').read())
    put_button(["What is Python ? "] , onclick=python)
    #python




    put_text("2: C#").style("font-size:24px")
    put_image(open('C:\\c#.png','rb').read())
    def csharp():
        put_text("                                   سي شارب                                                              ").style("font-size:50px")
        put_text("سي#  هي لغة برمجة متعددة الأنماط تتمتع بكونها سكونية التنميط وأمرية وتعريفية ووظيفية وتعتبر كائنية التوجُّه أو البرمجة الشيئية   وعمومية وشيئية المنحى (غرضية التوجه) (باستخدام الفئات) كما تخضع لمبادئ البرمجة التركيبية المنحى.").style('font-size:24px')
    put_button([' What is C# ?'],onclick=csharp)


    put_text("3 : C++").style("font-size:24px")
    put_image(open('C:\\c++.png','rb').read())
    def c():
        put_text( "                                    ++  سي                                                                   ").style( "font-size:50px")
        put_text("سي++ (تنطق: سي بلس بلس)  هي لغة برمجة كائنية، متعددة أنماط البرمجة، مصرفة، سكونية الأنماط. وتضم العديد من ميزات لغات البرمجة عالية المستوى ومنخفضة المستوى. بدأ تطوير هذه اللغة امتدادًا للغة سي تحت اسم (سي مع الأصناف) من قبل بيارن ستروستروب في مختبرات بل عام 1979 وأضيفت العديد من الميزات الأخرى لاحقاً وتغير الاسم عام 1983 ليصبح سي++  من باب الدعابة عبر استخدام معامل الزيادة لجانب اسم لغة سي تأكيداً على أنها لغة سي القادمة").style('font-size:24px')
    put_button([" What is c++ ? "],onclick=c)
    put_text("4 : JavaScript").style("font-size:24px")
    put_image(open('C:\\javascript.png', 'rb').read())
    def java():
               put_text( "                                    جافاسكريبت                                                                 ").style( "font-size:50px")
               put_text("بدأ استخدام الجافاسكريبت كلغة برمجة موجهة للمبرمجين الهواة وغير المحترفين. إلا أنه تزايد الاهتمام بها وجذبت اهتمام مبرمجين محترفين بعد إضافتها لتقنيات جديدة كانتشار تقنية اجاكس التي أدت إلى سرعة في التفاعل بين الخادم والعميل.تُستخدَم لغة الجافا سكربت في تطوير صفحات ويب تفاعلية، وتطبيقات الويب ، بما في ذلك الألعاب، وهي مُستعمَلة من أغلبية المواقع، وتدعمها جميع المتصفحات تقريبًا دون الحاجة إلى إضافات خارجية.").style('font-size:24px')


    put_button(['What is Java Script ? '],onclick=java)
    put_text("/")
    def btn_click():
        name = input('اكتب اسمك ! ',
                     type='text',
                     placeholder=" يفضل الكتابة بالانجليزية  ")
        put_text( " Hi  " + name).style('font-size:24px')
        put_text(   " ان الذكاء الاصطناعي يعمل بشكل اساسي على وضع شروط لتحقيقها  كما الان حين ضغطت الزر وظهرت لك واجهة تكتب فيها اسمك  ورحبت فيك عن طريق انك املأت متغير وبعدها قلت ان ينسخ اهلا  و يضيف اسمك فالشرط هنا هو استلام الاسم والضغط على الزر لكي اظهر لك الترحيب وهكذا يعمل الذكاء الاصطناعي لكن بتعمق اكبر و  بداتا بيز متعلمة اي لا تعتمد على معلومات محدده بل متجدده" ).style('font-size:24px')
    put_button([" Simple Logic : منطق بسيط "], onclick=btn_click )
    put_button(" مصمم هذا الموقع ", onclick=lambda: toast("مصمم هذا الموقع محمد عبد الخالق"))
    put_button(" تحت اشراف ", onclick=lambda: toast("ميس سمر والمكتب التنفيذي  "))

    def button():
        put_image(open('D:\\q.png', 'rb').read())
        put_image(open('D:\\w.png', 'rb').read())
        put_image(open('D:\\e.png', 'rb').read())
        put_image(open('D:\\r.png', 'rb').read())

    put_button("  مجلة الذكاء الاصطناعي تحت صنع المكتب التنفيذي     ", onclick=button)
if __name__ =="__main__":
    start_server(app,port=1039,debug=False)

