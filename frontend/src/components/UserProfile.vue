<template>
  <div v-if="profile" class="user-profile">
    <h1>User Profile</h1>
    <ul>
      <li><strong>First Name:</strong> {{ profile.first_name }}</li>
      <li><strong>Last Name:</strong> {{ profile.last_name }}</li>
      <li><strong>Email:</strong> {{ profile.email }}</li>
      <li><strong>NTNUI No:</strong> {{ profile.ntnui_no }}</li>
    </ul>
  </div>
  <p v-else-if="isLoading">Loading profile...</p>
  <p v-else>{{ error }}</p>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  setup() {
    const profile = ref(null);
    const error = ref('');
    const isLoading = ref(true);

    const fetchUserProfile = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/auth/user-profile/', {
          headers: {
            'Authorization': `Bearer ${localStorage.getItem('access_token')}`,
          },
        });
        if (response.status_code === 200) {
          profile.value = response.data;
          isLoading.value = false;
        } else {
          throw new Error(`Failed to fetch user profile: ${response.status_code}`);
        }
      } catch (err) {
        console.error('Error fetching profile:', err.response ? err.response.data : err);
        error.value = 'Error fetching profile: ' + (err.response ? err.response.data.error : err.message);
        isLoading.value = false;
      }
    };

    onMounted(fetchUserProfile);

    return {
      profile,
      error,
      isLoading,
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

.user-profile ul {
  list-style: none;
  padding: 0;
}

.user-profile li {
  padding: 10px 0;
  border-bottom: 1px solid #eee;
}

.user-profile li:last-child {
  border-bottom: none;
}

.user-profile strong {
  color: #555;
}
</style>
