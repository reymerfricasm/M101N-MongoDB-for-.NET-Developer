using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;

namespace M101DotNet.WebApp.Models
{
    public class Comment
    {
        // XXX WORK HERE
        // Add in the appropriate properties.
        // The homework instructions have the
        // necessary schema.
        /**
         * "Comments" : [
                {
                        "Author" : "Jack",
                        "Content" : "This is a comment.",
                        "CreatedAtUtc" : ISODate("2015-01-23T18:54:42.005Z")
                }
         * 
         */
         public string Author { get; set; }
         public string Content { get; set; }
        public DateTime CreatedAtUtc { get; set; }
    }
}
 