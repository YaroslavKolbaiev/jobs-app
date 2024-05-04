<script setup lang="ts">
import { Loader } from '@googlemaps/js-api-loader';

const { point } = defineProps<{
  point: string | undefined;
}>();

const API_KEY = import.meta.env.VITE_GOOGLE_MAPS_API_KEY;

const loader = new Loader({
  apiKey: API_KEY,
  version: 'weekly',
});

const location = point?.split('(')[1].split(')')[0].split(' ');

const lat = location ? +location[1] : 0;
const lng = location ? +location[0] : 0;

loader.load().then(async () => {
  // eslint-disable-next-line @typescript-eslint/ban-ts-comment
  // @ts-ignore
  const { Map } = await google.maps.importLibrary('maps');

  const map = new Map(document.getElementById('map') as HTMLElement, {
    center: { lat, lng },
    zoom: 15,
  });

  new google.maps.Marker({
    position: { lat, lng },
    map,
  });
});
</script>

<template>
  <div id="map" />
</template>

<style scoped lang="scss">
@import '../styles/mixins.scss';

#map {
  width: 100%;
  height: 240px;
  border-radius: 10px;
  margin-top: 20px;

  @include onTablet {
    height: 360px;
  }

  @include onDesktop {
    height: 240px;
  }
}
</style>
