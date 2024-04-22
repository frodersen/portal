require("dotenv").config();
const express = require("express");
const axios = require("axios");
const path = require("path");
const cookieParser = require("cookie-parser");

const app = express();
const PORT = process.env.PORT || 3002;

app.set("view engine", "ejs");
app.use(express.static("public"));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser());

app.get("/", async (req, res) => {
  const accessToken = req.cookies["access_token"];

  if (!accessToken) {
    return res.render("index");
  }

  try {
    const verifyResponse = await axios.post(
      "https://dev.api.ntnui.no/token/verify/",
      { token: accessToken }
    );

    if (verifyResponse.status === 401) {
      res.clearCookie("access_token");
      return res.render("index");
    }

    if (verifyResponse.status === 200) {
      // What if token is valid, but user is NOT authorized (should not have access to protected resource)?
      res.render("authorized");
    }

    console.log("Unexpected status code received:", verifyResponse.status);
    res.clearCookie("access_token");
    return res.render("index");
  } catch (error) {
    console.error(
      "Token verification network error:",
      error.response?.status,
      error.message
    );
    res.clearCookie("access_token");
    return res.render("index", {
      message: "Network error during authentication. Please try again.",
    });
  }
});

app.get("/auth/callback", async function (req, res) {
  const accessToken = req.cookies["access_token"];

  if (!accessToken) {
    return res.render("index");
  }

  try {
    const response = await axios.get(
      "https://dev.api.ntnui.no/users/profile/",
      {
        headers: { Authorization: "Bearer " + accessToken },
      }
    );

    const userMemberships = response.data.memberships;
    const clientGroupName = process.env.CLIENT_GROUP_NAME;
    let isMember = false;

    for (let i = 0; i < userMemberships.length; i++) {
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
  } catch (error) {
    console.error(
      "Error fetching user profile:",
      error.response ? error.response.data : error
    );
    res.status(500).send("Failed to fetch user profile data");
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
