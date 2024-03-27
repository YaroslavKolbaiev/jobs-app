# Jobs App

// const { error, setError } = useError();
// const { isLoading, setIsLoading } = useIsLoading();

// const jobs = ref<Job[]>([]);

// onMounted(async () => {
// setIsLoading(true);
// try {
// const data = await getJobs();
// jobs.value = data.jobs;
// throw data;
// } catch (err: unknown) {
// if (err instanceof Error) {
// setError(err);
// }
// } finally {
// setIsLoading(false);
// }
// });

const location = point?.split('(')[1].split(')')[0].split(' ');

const lat = location ? location[0] : 0;

<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBNLrJhOMz6idD05pzfn5lhA-TAw-mAZCU&callback=Function.prototype"></script>

let map: google.maps.Map;

onMounted(() => {
const mapOptions: google.maps.MapOptions = {
center: { lat, lng },
zoom: 15,
};
map = new google.maps.Map(
document.getElementById('mapId') as HTMLElement,
mapOptions
);
new google.maps.Marker({
position: { lat, lng },
map,
});
});
