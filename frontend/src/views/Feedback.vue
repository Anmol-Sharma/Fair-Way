<script setup>
import { ref } from "vue";

sessionStorage.clear();

const userName = ref("");
const mailId = ref("");
const feedbackText = ref("");

async function handleSubmit(event) {
  const feedbackData = {
    name: userName.value,
    email: mailId.value || null, // Handles optional email
    feedback: feedbackText.value,
  };

  try {
    // Initialize request configuration with default method and body
    const req = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(feedbackData),
    };

    // Upload the file to backend system for processing
    const response = await fetch("/api/Feedback", req);

    // Check for HTTP 500 error
    if (response.status === 500) {
      router.push({ name: "500" });
      throw new Error("Internal Server Error");
    }

    if (response.status !== 201) {
      alert("Error while processing your feedback. We'll look into it.");
      throw new Error(`HTTP response code ${response.status}. Data has not been accepted.`);
    }

    alert("Thanks for you Feedback");
    // Clear form fields after submission
    userName.value = "";
    mailId.value = "";
    feedbackText.value = "";
  } catch (error) {
    console.error("Error submitting feedback:", error);
    alert("Failed to submit feedback. Please try again.");
  }
}
</script>
<template>
  <div
    class="container-fluid main-container d-flex justify-content-center align-content-center my-5"
  >
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">General Feedbacks are always Welcome!</h5>
        <p class="card-text my-4">Please provide your feedback below.</p>
        <form @submit.prevent="handleSubmit($event)">
          <div class="row my-3">
            <div class="col-2 text-end">
              <label for="userName" class="col-form-label">Name</label>
            </div>
            <div class="col">
              <input type="text" class="form-control" required id="userName" v-model="userName" />
            </div>
          </div>
          <div class="row my-3">
            <div class="col-2 text-end">
              <label for="mailId" class="col-form-label">Email (Optional)</label>
            </div>
            <div class="col">
              <input
                type="email"
                class="form-control"
                id="mailId"
                placeholder="Your Email Address"
                v-model="mailId"
              />
            </div>
          </div>
          <div class="row my-3">
            <div class="col-2 text-end">
              <label for="feedbackText" class="col-form-label">Feedback</label>
            </div>
            <div class="col">
              <textarea
                class="form-control"
                id="feedbackText"
                required
                rows="12"
                placeholder="If you encountered any errors please provide detailed feedback."
                v-model="feedbackText"
              ></textarea>
            </div>
          </div>
          <div class="text-center">
            <button type="submit" class="btn btn-primary">Submit Feedback</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-container {
  background-color: #ffffff;
}

.form-control {
  width: 80%;
}

.card-title {
  font-size: 2.5rem;
}

.card-text {
  font-size: 1.2rem;
  margin: 5px;
}

.btn {
  position: relative;
}

.card-body {
  min-width: 70rem;
  min-height: 30rem;
}
</style>
