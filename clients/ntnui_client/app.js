require("dotenv").config();
const express = require("express");
const session = require("express-session");
const axios = require("axios");
const path = require("path");
const cookieParser = require("cookie-parser");

const app = express();
const PORT = process.env.PORT || 3001;

app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());
app.use(
  session({
    secret: "your secret key",
    resave: false,
    saveUninitialized: true,
    cookie: { secure: false }, // Use secure: true in production
  })
);

// INITIAL PAGE
app.get("/", (req, res) => {
  res.render("index");
});

app.get("/auth/callback", function (req, res) {
  try {
    var accessToken = req.cookies["access_token"];

    axios
      .get("https://dev.api.ntnui.no/users/profile/", {
        headers: { Authorization: "Bearer " + accessToken },
      })
      .then(function (response) {
        var userMemberships = response.data.memberships;
        var clientGroupName = process.env.CLIENT_GROUP_NAME;
        var isMember = false;

        for (var i = 0; i < userMemberships.length; i++) {
          if (userMemberships[i].slug === clientGroupName) {
            isMember = true;
            break;
          }
        }

        if (isMember) {
          res.render("authorized");
        } else {
          res.render("unauthorized");
        }
      })
      .catch(function (error) {
        console.error("Error fetching user profile:", error);
        res.status(500).send("Failed to fetch user profile data");
      });
  } catch (error) {
    console.error("Error in processing:", error);
    res.status(500).send("Server error");
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
