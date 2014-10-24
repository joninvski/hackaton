using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using WalletSaverDashboards.Models;

namespace WalletSaverDashboards.Providers
{
    public class CompanyDataProvider
    {
        public static Company GetData()
        {
            return new Company
            {
                name = "Test",
                employees = new List<Employee>()
                {
                    new Employee
                    {
                        name = "António",
                        phoneNumbers = new List<PhoneNumber>()
                        {
                            new PhoneNumber
                            {
                                number = 911111111,
                                minutes = 1111,
                                messageNumber = 111
                            }
                        }
                    },
                    new Employee
                    {
                        name = "João",
                        phoneNumbers = new List<PhoneNumber>()
                        {
                            new PhoneNumber
                            {
                                number = 922222222,
                                minutes = 2222,
                                messageNumber = 222
                            }
                        }
                    },
                    new Employee
                    {
                        name = "Jiacopo",
                        phoneNumbers = new List<PhoneNumber>()
                        {
                            new PhoneNumber
                            {
                                number = 933333333,
                                minutes = 3333,
                                messageNumber = 333
                            }
                        }
                    },
                    new Employee
                    {
                        name = "Giacomo",
                        phoneNumbers = new List<PhoneNumber>()
                        {
                            new PhoneNumber
                            {
                                number = 944444444,
                                minutes = 4444,
                                messageNumber = 4444
                            }
                        }
                    }
                }
            };
        }
    }
}