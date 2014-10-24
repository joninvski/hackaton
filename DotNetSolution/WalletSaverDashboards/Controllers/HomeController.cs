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


            return View(new Home { total_seconds = 999999999, total_msg = 1111, total_trafic = 2222});
        }
    }
}
