using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using WalletSaverDashboards.Models;
using WalletSaverDashboards.Providers;

namespace WalletSaverDashboards.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            ViewBag.Title = "Home Page";


            return View(new Home { total_calls_incoming = 111, total_calls_outgoing= 222, total_data_incoming = 333, total_data_outgoing = 444, total_messages_incoming = 555, total_messages_outgoing = 666});
        }

        public ActionResult Calls()
        {
            return View();
        }

        public ActionResult Data()
        {
            return View();
        }

        public ActionResult Messages()
        {
            return View();
        }

    }
}
