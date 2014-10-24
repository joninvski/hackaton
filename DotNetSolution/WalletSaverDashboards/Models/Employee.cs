using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WalletSaverDashboards.Models
{
    public class Employee
    {
        public string name { get; set; }
        public List<PhoneNumber> phoneNumbers { get; set; }
    }
}