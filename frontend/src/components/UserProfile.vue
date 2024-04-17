<template>
  <div v-if="profile" class="user-profile">
    <h1>User Profile</h1>
    <!-- Display the profile as JSON -->
    <pre>{{ jsonProfile }}</pre>
  </div>
  <p v-else-if="isLoading">Loading profile...</p>
  <p v-else>{{ error }}</p>
</template>

<script>
import { ref, onMounted, computed } from "vue";
import axios from "axios";

export default {
  setup() {
    const profile = ref(null);
    const error = ref("");
    const isLoading = ref(true);

    const fetchUserProfile = async () => {
      isLoading.value = true;
      try {
        const response = await axios.get(
          "http://127.0.0.1:8000/auth/user-profile/",
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem("access_token")}`,
            },
          }
        );
        profile.value = response.data;
        error.value = "";
      } catch (err) {
        console.error("Error fetching profile:", err);
        error.value = "Failed to fetch profile.";
        profile.value = null;
      }
      isLoading.value = false;
    };

    onMounted(fetchUserProfile);

    const jsonProfile = computed(() => {
      return profile.value ? JSON.stringify(profile.value, null, 2) : "{}";
    });

    return {
      profile,
      error,
      isLoading,
      jsonProfile,
    };
  },
};
</script>

<style scoped>
.user-profile {
  background-color: #ffffff;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  margin: 20px auto;
}

.user-profile h1 {
  color: #333;
  text-align: center;
}

pre {
  background-color: #f4f4f4;
  border: 1px solid #ddd;
  padding: 10px;
  border-radius: 5px;
  overflow: auto;
}
</style>
