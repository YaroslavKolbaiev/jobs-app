<script setup lang="ts">
import IconLoader from "@/components/icons/IconLoader.vue";
import useFetchData from "../../hooks/useFetchData";
import { uploadResume } from "@/api/auth";
import { ref, watch } from "vue";
import { useAuthStore } from "@/stores/auth";

const emit = defineEmits(["errorEmited"]);
const resume = ref();
const resumeName = ref("");
const progress = ref(0);
const useAuth = useAuthStore();

const onUploadResume = async () => {
  const formData = new FormData();
  formData.append("resume", resume.value);

  await uploadResume(formData, (progressEvent) => {
    progress.value = Math.round(
      (progressEvent.loaded * 100) / (progressEvent.total ?? 1)
    );
  });
  if (useAuth.user) {
    useAuth.user.resume = resume.value;
  }
};

const { isLoading, error, doRequest } = useFetchData(onUploadResume);

watch(error, () => {
  emit("errorEmited", error);
});
</script>

<template>
  <form class="form grid__item--1-6" @submit.prevent="doRequest">
    <h2>Upload Resume</h2>
    <input
      type="file"
      name="resume"
      id="fileInput"
      accept=".pdf,.doc,.docx"
      @change="
        (e) => {
          resume = (e.currentTarget as HTMLInputElement)?.files?.[0];
          resumeName = resume?.name;
        }
      "
    />
    <div class="flex-start-center">
      <label for="fileInput"> Choose File </label>
      <span>{{ resumeName }}</span>
    </div>
    <progress :value="progress" max="100"></progress>
    <button :disabled="isLoading" type="submit" class="button">
      <IconLoader v-if="isLoading" />
      <span v-else>Submit</span>
    </button>
  </form>
</template>

<style scoped lang="scss">
@import "../../styles/buttons.scss";

h2 {
  margin: 0;
}

progress {
  width: 100%;
  margin-bottom: 10px;
  appearance: none;
}

progress::-webkit-progress-bar {
  background-color: var(--main-bg);
  border: 1px solid var(--c-gray);
  border-radius: 10px;
}

progress::-webkit-progress-value {
  background-color: var(--c-blue);
  border-radius: 10px;
}

input[type="file"] {
  display: none;
}

label {
  padding: 10px 20px;
  background-color: #dedede;
  color: var(--c-gray);
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 96px;
  text-align: center;
}
</style>
