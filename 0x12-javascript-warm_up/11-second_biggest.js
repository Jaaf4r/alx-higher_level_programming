if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number).sort();
  for (let i = args.length - 2; i >= 0; i--) {
    if (args[i] !== args[args.length - 1]) {
      console.log(args[i]);
      break;
    }
  }
}
