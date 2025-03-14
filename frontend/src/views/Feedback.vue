<script setup>
import router from "../router";
import { ref } from "vue";

const userName = ref("");
const mailId = ref("");
const feedbackText = ref("");

async function handleSubmit(event) {
  const feedbackData = {
    name: userName.value,
    email: mailId.value || null, // Handles optional email
    feedback: feedbackText.value,
  };

  // TODO: Handle with the updated postdata code setup
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
            <div class="col-md-2 col-12 text-md-end text-start mb-2 mb-md-0">
              <label for="userName" class="col-form-label">Name</label>
            </div>
            <div class="col-md-10 col-12">
              <input type="text" class="form-control" required id="userName" v-model="userName" />
            </div>
          </div>
          <div class="row my-3">
            <div class="col-md-2 col-12 text-md-end text-start mb-2 mb-md-0">
              <label for="mailId" class="col-form-label">Email (Optional)</label>
            </div>
            <div class="col-md-10 col-12">
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
            <div class="col-md-2 col-12 text-md-end text-start mb-2 mb-md-0">
              <label for="feedbackText" class="col-form-label">Feedback</label>
            </div>
            <div class="col-md-10 col-12">
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
          <div class="text-center mt-4">
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
  width: 100%;
  padding: 0 15px;
}

.card {
  width: 100%;
  max-width: 1200px;
}

.card-body {
  width: 100%;
  min-height: 30rem;
  padding: 1.5rem;
}

.form-control {
  width: 100%;
}

.card-title {
  font-size: 2.5rem;
  text-align: center;
}

@media (max-width: 992px) {
  .card-title {
    font-size: 1.8rem;
  }

  .card-text {
    font-size: 1rem;
  }

  .card-body {
    min-height: auto;
    padding: 1rem;
  }
}

@media (max-width: 768px) {
  .card-title {
    font-size: 1.5rem;
  }
}

.card-text {
  font-size: 1.2rem;
  margin: 5px;
  text-align: center;
}

.btn {
  position: relative;
}

.row {
  margin-right: 0;
  margin-left: 0;
  width: 100%;
}
</style>
