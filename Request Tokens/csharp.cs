using System;
using System.Linq;
using System.Text;
using System.Security.Cryptography;

namespace SnapchatReqToken
{
    class Program
    {
        static string hashPattern = "0001110111101110001111010101111011010001001110011000110001000110";
        static string secret = "iEk21fuwZApXlz93750dmW22pw389dPwOk";

        static void Main(string[] args)
        {
            Console.WriteLine(requestToken("m198sOkJEn37DjqZ32lpRu76xmw288xSQ9", timestamp()));

            Console.ReadLine();
        }

        public static string timestamp()
        {
            return Convert.ToInt64(Math.Round((DateTime.UtcNow - new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc)).TotalSeconds * 1000)).ToString();
        }

        public static string sha256(string data)
        {
            byte[] hash = new SHA256Managed().ComputeHash(Encoding.UTF8.GetBytes(data));

            return hash.Aggregate(string.Empty, (current, x) => current + String.Format("{0:x2}", x));
        }

        public static string requestToken(string token, string timestamp)
        {
            string firstHash = sha256(secret + token);
            string secondHash = sha256(timestamp + secret);

            string result = "";

            for (int i = 0; i < hashPattern.Length; i++)
            {
                if (hashPattern[i] == '0')
                    result += firstHash[i];
                else
                    result += secondHash[i];
            }

            return result;
        }
    }
}
