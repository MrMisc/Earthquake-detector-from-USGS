
async def time_check():
    await client.wait_until_ready()
    channel = client.get_channel(400673288768192524)
    mainchannel = client.get_channel(83566743976411136)
    rss_address = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_day.geojson"
    json_data = requests.get(rss_address).json()
    magn = float(json_data['features'][0]['properties']['mag'])
    loc = json_data['features'][0]['properties']['place']
    sham = await client.fetch_user(305647375756689429)
    global n
    if (magn >= 5.6) and (loc not in n):      #Checks if read recent earthquake is above magnitude or equal to 5.6
        print(n)
        n.append(loc)
        await sham.send(f'``WARNING:{loc} with a magnitude of {magn} recently!``')
        await mainchannel.send(f'``WARNING:{loc} with a magnitude of {magn}!``')
        if len(n)>=10:
            n = n[0:1]
    await asyncio.sleep(1800)