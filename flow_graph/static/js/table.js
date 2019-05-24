
$(document).ready(function()
{
    $('.data_table').DataTable(
    {
        "paging":   false,
        "searching": false,
        "info": false,
        "responsive": true,
        "order": [[ 0, "desc" ]]
    })

    var numberOfData = 15

    // Fill color for clean display
    $(".indic").each(function(i)
    {
        let value = $(this).data("value")

        console.log(value)

        if (value == 'None')
        {
            $(this).text("-")
        }

        // We want only red/green for non forced
        if(i%numberOfData == 11)
        {
            if (value.toLowerCase() == 'oui')
            {
                $(this).addClass("table-bg-5")
            }else
            {
                $(this).addClass("table-bg-1")
            }
        }
        else if (i%numberOfData == 13)
        {
            value = (5 - value) + 1
            $(this).addClass("table-bg-"+value)
        }
        // We want color for social ambiance good/none/bad
        else if (i%numberOfData == 14)
        {
            switch(value.toLowerCase())
            {
                case 'bonne':
                    $(this).addClass("table-bg-5")
                    break
                case 'neutre':
                    $(this).addClass("table-bg-3")
                    break
                case 'négative':
                    $(this).addClass("table-bg-1")
                    break
            }
        }
        else
        {
            // Round if this is the first element of each row (flow indicator)
            if(i%numberOfData == 0)
            {
               value = Math.round(parseFloat(value))
            }
            console.log(value)
            $(this).addClass("table-bg-"+value)
        }
    })

    // Theoretical flow
    $(".theoretical_flow").each(function(i){
        let value = $(this).data("value")
        let canal = 0

        switch(value.toLowerCase())
        {
            case 'stimulé':
                canal = 1
                break
            case 'flow':
                canal = 2
                break
            case 'contrôle':
                canal = 3
                break
            case 'relaxation':
                canal = 4
                break
            case 'ennui':
                canal = 5
                break
            case 'apathie':
                canal = 6
                break
            case 'inquietude':
                canal = 7
                break
            case 'angoisse':
                canal = 8
                break
        }

        $(this).addClass("flow-"+canal)
    })
})