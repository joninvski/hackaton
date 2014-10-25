using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace WalletSaverDashboards.Models
{
    public class Home
    {
        public int total_calls_outgoing { get; set; }
        public int total_calls_incoming { get; set; }
        public int total_messages_outgoing { get; set; }
        public int total_messages_incoming { get; set; }
        public int total_data_outgoing { get; set; }
        public int total_data_incoming { get; set; }
    }
}