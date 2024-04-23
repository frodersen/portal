require("dotenv").config();
const express = require("express");
const axios = require("axios");
const cookieParser = require("cookie-parser");

const app = express();
const PORT = process.env.PORT || 3001;

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

    if (verifyResponse.status !== 200) {
      res.clearCookie("access_token");
      return res.render("index");
    }

    const response = await axios.get(
      "https://dev.api.ntnui.no/users/profile/",
      {
        headers: { Authorization: "Bearer " + accessToken },
      }
    );

    const userMemberships = response.data.memberships;
    const clientGroupName = process.env.CLIENT_GROUP_NAME;
    let isMember = userMemberships.some((m) => m.slug === clientGroupName);

    if (isMember) {
      res.render("authorized");
    } else {
      res.render("unauthorized");
    }
  } catch (error) {
    console.error(
      "Error during authentication or profile fetching:",
      error.response ? error.response.data : error
    );
    res.clearCookie("access_token");
    res.status(500).send("Failed to authenticate or fetch profile data.");
  }
});

app.get("/logout", (req, res) => {
  res.clearCookie("access_token");
  res.redirect("/");
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
