using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace M101DotNet.WebApp.Models
{
    public class Post
    {
        // XXX WORK HERE
        // add in the appropriate properties for a post
        // The homework instructions contain the schema.
        /*
         * "_id" : ObjectId("54c298ec122ea911588b7970"),
        "Author" : "Craig",
        "Title" : "Frist!!!",
        "Content" : "This is my first post!!!",
        "Tags" : [
                "first",
                "awesome"
        ],
        "CreatedAtUtc" : ISODate("2015-01-23T18:54:36.335Z"),
        "Comments" : [
                {
                        "Author" : "Jack",
                        "Content" : "This is a comment.",
                        "CreatedAtUtc" : ISODate("2015-01-23T18:54:42.005Z")
                }
        ]
}
         */

        [BsonRepresentation(BsonType.ObjectId)]
        public int Id { get; set; }
        public string Author { get; set; }
        public string Title { get; set; }
        public string Content { get; set; }
        public string Tags { get; set; }
        public DateTime CreatedAtUtc { get; set; }
        public List<Comment> Comments { get; set; }

        public Post()
        {
            Comments = new List<Comment>();
        }
    }
}