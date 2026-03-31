
using System.Text.Json;

namespace Develop02
{
    public class UserEntry
    {
        public DateTime CurrentDateTime { get; set; } = DateTime.Now;
        public string UserTextEntry { get; set; } = "";
        public string UserMood { get; set; } = "";
        public string GivenPrompt { get; set; } = RandomPromptGenerator.GetRandomPrompt();

        public string MakeEntry()
        {
            return $"{CurrentDateTime}\nRandom Prompt: {GivenPrompt}\n{UserTextEntry}\nToday's Mood: {UserMood}";
        }
    }

    public class Journal
    {
        public List<UserEntry> Entries { get; set; } = new List<UserEntry>();

        public void AddEntry(UserEntry userEntry)
        {
            Entries.Add(userEntry);
        }



        public void SaveEntries(string fileName)
        {
            string json = JsonSerializer.Serialize(Entries, new JsonSerializerOptions { WriteIndented = true });
            File.WriteAllText(fileName, json);
        }



        public void LoadEntries(string fileName)
        {
            string json = File.ReadAllText(fileName);
            Entries = JsonSerializer.Deserialize<List<UserEntry>>(json);
        }
    }
}