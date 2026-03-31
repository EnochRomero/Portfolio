
class Reflecting : Activity
{
        List<string> expereincePrompts = new List<string>
    {
        "Think of a time you felt truly proud of yourself",
        "Think of a time you overcame something difficult",
        "Think of a moment when you felt completely at peace",
        "Think of a time you helped someone in a meaningful way",
        "Think of a time you learned an important life lesson",
        "Think of a moment when you stepped outside your comfort zone",
        "Think of a time you felt deeply grateful",
        "Think of a time you handled a situation better than you expected",
        "Think of a moment when you felt supported by someone else",
        "Think of a time you had to make a hard decision",
        "Think of a moment that changed your perspective",
        "Think of a time you showed resilience during a setback",
        "Think of a moment when you felt genuinely happy",
        "Think of a time you discovered something new about yourself",
        "Think of a time you forgave someone or yourself"
    };

    List<string> reflectionQuestions = new List<string>
    {
        "What did that experience teach you about yourself?",
        "How did that experience make you feel at the time?",
        "What strengths did you use during that experience?",
        "What would you do differently if it happened again?",
        "How did that experience affect your relationships with others?",
        "What did you learn about your values or priorities?",
        "How has that experience shaped your choices since then?",
        "What challenges did you face and how did you overcome them?",
        "How did this experience change your perspective on life?",
        "What positive outcomes came from this experience, even if small?"
    };

    public void ReflectingActicity()
    {
        Random random = new Random();

        int index = random.Next(expereincePrompts.Count);
        string randomPrompt = expereincePrompts[index];

        Console.WriteLine($"---{randomPrompt}---");

        Console.WriteLine($"When you have an experience in mind, press enter.");

        Console.ReadLine();

        Console.WriteLine($"Now you will ponder the following questions as they relate to your expereience. ");
        Console.Write($"You will begin in: ");        

        int countDown = 4;
        while (countDown > -1)
            {
                Console.Write("\b \b");
                if (countDown >= 1) 
                { 
                    Console.Write(countDown);
                }
                Thread.Sleep(1000);
                countDown -= 1;
            }

        Console.Clear();

        DateTime startTime = DateTime.Now;
        DateTime endTime = startTime.AddSeconds(GetDuration());

        while (DateTime.Now < endTime)
        {
            int reflectionIndex = random.Next(reflectionQuestions.Count);
            string relfectionPrompt = reflectionQuestions[reflectionIndex];
            Console.WriteLine($"---{relfectionPrompt}---");
            DisplayLoadingAnimation(10);
        }


    }




}